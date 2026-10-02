from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.forms import AwardForm
from main.models import Award, Experience


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=timezone.now(),
        )
        self.award = Award.objects.create(
            title="ICPC Asia Jakarta",
            recognition="Highest Honors · Rank 22",
            description="Recognized at the ICPC Asia Jakarta regional contest.",
            awarded_at=timezone.datetime(2025, 1, 1).date(),
        )
        self.superuser = User.objects.create_superuser(
            username="owner",
            password="test-password",
        )
        self.editor = User.objects.create_user(
            username="editor",
            password="test-password",
        )
        editor_group, _ = Group.objects.get_or_create(name="Editor")
        self.editor.groups.add(editor_group)

    def test_main_page_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertContains(response, "Things I Do")
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_collection_pages_render_ajax_shells_instead_of_initial_records(self):
        awards_response = self.client.get(reverse("main:show_awards"))
        experiences_response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(awards_response.status_code, 200)
        self.assertTemplateUsed(awards_response, "awards.html")
        self.assertContains(awards_response, 'id="grid"')
        self.assertContains(awards_response, "fetchAwards")
        self.assertNotContains(awards_response, self.award.title)
        self.assertEqual(experiences_response.status_code, 200)
        self.assertTemplateUsed(experiences_response, "experience.html")
        self.assertContains(experiences_response, 'id="timeline"')
        self.assertContains(experiences_response, "fetchExperiences")
        self.assertNotContains(experiences_response, self.experience.title)

    def test_awards_api_returns_manual_json_and_filters_by_title(self):
        response = self.client.get(
            reverse("main:get_awards_json"),
            {"title": "jakarta"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.json(), [
            {
                "pk": str(self.award.id),
                "fields": {
                    "title": self.award.title,
                    "recognition": self.award.recognition,
                    "description": self.award.description,
                    "image": self.award.image,
                    "star_count": 0,
                    "is_starred": False,
                    "starred_by_names": "",
                    "awarded_at": "2025-01-01",
                },
            }
        ])

    def test_experiences_api_returns_manual_json_and_filters_by_title(self):
        response = self.client.get(
            reverse("main:get_experiences_json"),
            {"title": "dosen"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "application/json")
        payload = response.json()
        self.assertEqual(len(payload), 1)
        self.assertEqual(payload[0]["pk"], str(self.experience.id))
        self.assertEqual(payload[0]["fields"]["title"], self.experience.title)
        self.assertEqual(payload[0]["fields"]["category_display"], "Part-Time")
        self.assertTrue(payload[0]["fields"]["is_ongoing"])
        self.assertEqual(payload[0]["fields"]["star_count"], 0)
        self.assertFalse(payload[0]["fields"]["is_starred"])

    def test_collection_api_reports_star_state_for_authenticated_user(self):
        self.award.starred_by.add(self.editor)
        self.experience.starred_by.add(self.editor)
        self.client.force_login(self.editor)

        awards_response = self.client.get(reverse("main:get_awards_json"))
        experiences_response = self.client.get(reverse("main:get_experiences_json"))

        award_fields = awards_response.json()[0]["fields"]
        experience_fields = experiences_response.json()[0]["fields"]
        self.assertTrue(award_fields["is_starred"])
        self.assertEqual(award_fields["star_count"], 1)
        self.assertEqual(award_fields["starred_by_names"], "editor")
        self.assertTrue(experience_fields["is_starred"])
        self.assertEqual(experience_fields["star_count"], 1)
        self.assertEqual(experience_fields["starred_by_names"], "editor")

    def test_ajax_create_endpoints_only_allow_post(self):
        for route_name in ("main:create_award_ajax", "main:create_experience_ajax"):
            response = self.client.get(reverse(route_name))
            self.assertEqual(response.status_code, 405)

    def test_ajax_create_endpoints_return_json_for_anonymous_user(self):
        for route_name in ("main:create_award_ajax", "main:create_experience_ajax"):
            response = self.client.post(reverse(route_name), {})
            self.assertEqual(response.status_code, 403)
            self.assertEqual(response["Content-Type"], "application/json")
            self.assertIn("message", response.json())

    def test_ajax_create_endpoints_return_validation_errors_for_owner(self):
        self.client.force_login(self.superuser)

        for route_name in ("main:create_award_ajax", "main:create_experience_ajax"):
            response = self.client.post(reverse(route_name), {})
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response["Content-Type"], "application/json")
            self.assertIn("errors", response.json())

    def test_owner_can_create_award_over_ajax(self):
        self.client.force_login(self.superuser)

        response = self.client.post(
            reverse("main:create_award_ajax"),
            {
                "title": "OSN 2024",
                "recognition": "Silver Medal",
                "description": "National olympiad achievement.",
                "image": "https://example.com/osn.png",
                "awarded_at": "2024-01-01",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response["Content-Type"], "application/json")
        created_award = Award.objects.get(pk=response.json()["pk"])
        self.assertEqual(created_award.title, "OSN 2024")

    def test_owner_can_create_completed_experience_over_ajax(self):
        self.client.force_login(self.superuser)

        response = self.client.post(
            reverse("main:create_experience_ajax"),
            {
                "title": "Research Assistant",
                "description": "Built reproducible experiments.",
                "category": "research",
                "started_at": "2025-01-01T09:00",
                "ended_at": "2025-06-01T17:00",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response["Content-Type"], "application/json")
        created_experience = Experience.objects.get(pk=response.json()["pk"])
        self.assertEqual(created_experience.title, "Research Assistant")
        self.assertFalse(created_experience.is_ongoing)

    def test_editor_can_update_existing_records(self):
        self.client.force_login(self.editor)

        experience_response = self.client.post(
            reverse("main:update_experience", args=[self.experience.id]),
            {
                "title": "Updated Experience",
                "description": "Updated description.",
                "category": "research",
                "started_at": "2025-01-01T09:00",
                "ended_at": "2025-06-01T17:00",
            },
        )
        award_response = self.client.post(
            reverse("main:update_award", args=[self.award.id]),
            {
                "title": "Updated Award",
                "recognition": "Updated recognition",
                "description": "Updated description",
                "image": "https://example.com/updated.jpg",
                "awarded_at": "2025-01-01",
            },
        )

        self.assertRedirects(experience_response, reverse("main:show_experience"))
        self.assertRedirects(award_response, reverse("main:show_awards"))
        self.experience.refresh_from_db()
        self.award.refresh_from_db()
        self.assertEqual(self.experience.title, "Updated Experience")
        self.assertEqual(self.award.title, "Updated Award")

    def test_award_form_strips_html_from_text_fields(self):
        form = AwardForm({
            "title": "<b>Safe title</b>",
            "recognition": "<i>Recognition</i>",
            "description": "<script>alert(1)</script>Description",
            "image": "https://example.com/award.png",
            "awarded_at": "2025-01-01",
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["title"], "Safe title")
        self.assertEqual(form.cleaned_data["recognition"], "Recognition")
        self.assertEqual(form.cleaned_data["description"], "alert(1)Description")

    def test_mobile_navigation_uses_native_details_menu(self):
        for route_name in ("main:show_main", "main:show_experience", "main:show_awards"):
            response = self.client.get(reverse(route_name))

            self.assertContains(response, 'class="site-menu"')
            self.assertContains(response, '<summary class="menu-toggle">')
            self.assertContains(response, 'class="site-nav"')
            self.assertContains(response, 'href="/awards/"')
            self.assertNotContains(response, 'src="/static/js/nav.js"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)
