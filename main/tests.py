from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Award, Experience


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
            started_at=timezone.now(),
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_things_i_do_section_lists_selected_interests(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertContains(response, "Things I Do")
        for interest in (
            "Competitive Programming",
            "Learning about AI",
            "Reading Comics",
            "Listening to Music",
        ):
            self.assertContains(response, interest)

    def test_awards_page_reads_awards_from_the_database(self):
        Award.objects.create(
            title="ICPC Asia Jakarta",
            recognition="Highest Honors · Rank 22",
            description="Recognized at the ICPC Asia Jakarta regional contest.",
            awarded_at=timezone.datetime(2025, 1, 1).date(),
        )

        response = self.client.get(reverse("main:show_awards"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "awards.html")
        self.assertContains(response, "Awards & Achievements")
        self.assertContains(response, "ICPC Asia Jakarta")
        self.assertContains(response, "2025")
        self.assertContains(response, "Highest Honors · Rank 22")
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_awards_page_renders_empty_photo_placeholder(self):
        Award.objects.create(
            title="OSN 2024",
            recognition="Silver Medal",
            description="National-level computer science olympiad achievement.",
            awarded_at=timezone.datetime(2024, 1, 1).date(),
        )

        response = self.client.get(reverse("main:show_awards"))

        self.assertContains(response, "OSN 2024")
        self.assertContains(response, "Silver Medal")
        self.assertContains(response, 'class="award-image-placeholder"')

    def test_empty_awards_page(self):
        response = self.client.get(reverse("main:show_awards"))

        self.assertContains(response, "There is no award or achievement added yet.")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, 'class="experience-marker"')
        self.assertContains(response, 'class="experience-entry-heading"')
        self.assertContains(response, 'class="experience-entry-content"')
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "There is no experience added yet.")

    def test_mobile_navigation_uses_native_details_menu(self):
        for route in ("main:show_main", "main:show_experience", "main:show_awards"):
            response = self.client.get(reverse(route))

            self.assertContains(response, 'class="site-menu"')
            self.assertContains(response, '<summary class="menu-toggle">')
            self.assertContains(response, 'class="site-nav"')
            self.assertContains(response, 'href="/awards/"')
            self.assertNotContains(response, 'href="/#highlights"')
            self.assertNotContains(response, 'src="/static/js/nav.js"')

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Finished")
        self.assertNotContains(response, "Ongoing")