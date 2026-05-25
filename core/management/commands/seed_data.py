import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from campuses.models import Campus
from sermons.models import Speaker, Series, Sermon
from events.models import Event
from donations.models import Campaign
from prayers.models import PrayerRequest
from groups.models import GroupCategory, MinistryGroup

class Command(BaseCommand):
    help = 'Seeds the database with realistic sample content for St. Bottle Cathedral'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # 1. Create Campuses
        Campus.objects.all().delete()
        c1 = Campus.objects.create(name="Downtown Campus", slug="downtown", address="123 Faith Avenue, Holy City, HC 12345", timezone="UTC", contact_email="downtown@stbottle.org")
        c2 = Campus.objects.create(name="Northside Campus", slug="northside", address="456 Grace Blvd, Holy City, HC 12346", timezone="UTC", contact_email="northside@stbottle.org")
        c3 = Campus.objects.create(name="Online Global", slug="online", address="Everywhere", timezone="UTC", contact_email="online@stbottle.org")
        campuses = [c1, c2, c3]
        self.stdout.write("Created 3 Campuses.")

        # 2. Create Speakers & Series for Sermons
        Speaker.objects.all().delete()
        Series.objects.all().delete()
        Sermon.objects.all().delete()

        sp1 = Speaker.objects.create(name="Pastor John Smith", bio="Lead Pastor of St. Bottle Cathedral.")
        sp2 = Speaker.objects.create(name="Reverend Jane Doe", bio="Associate Pastor and Community Leader.")

        ser1 = Series.objects.create(title="The Book of Romans", description="A deep dive into Paul's letter to the Romans.")
        ser2 = Series.objects.create(title="Finding Purpose", description="Discovering God's calling for your life.")

        now = timezone.now()

        # 3. Create 5 Sermons
        Sermon.objects.create(
            title="Faith and Righteousness", date=(now - timedelta(days=7)).date(), passage="Romans 1:16-17",
            speaker=sp1, series=ser1, campus=c1, video_url="https://youtube.com", transcript="This is the transcript of Faith and Righteousness."
        )
        Sermon.objects.create(
            title="Grace Abounding", date=(now - timedelta(days=14)).date(), passage="Romans 5:20",
            speaker=sp1, series=ser1, campus=c1, video_url="https://youtube.com"
        )
        Sermon.objects.create(
            title="Your Unique Calling", date=(now - timedelta(days=21)).date(), passage="Ephesians 2:10",
            speaker=sp2, series=ser2, campus=c2, video_url="https://youtube.com"
        )
        Sermon.objects.create(
            title="Walking in the Spirit", date=(now - timedelta(days=28)).date(), passage="Romans 8:1-4",
            speaker=sp1, series=ser1, campus=c1, video_url="https://youtube.com"
        )
        Sermon.objects.create(
            title="The Cost of Discipleship", date=(now - timedelta(days=35)).date(), passage="Luke 14:25-33",
            speaker=sp2, series=ser2, campus=c3, video_url="https://youtube.com"
        )
        self.stdout.write("Created 5 Sermons with Speakers and Series.")

        # 4. Create 4 Upcoming Events
        Event.objects.all().delete()
        Event.objects.create(
            title="Sunday Morning Worship", description="Join us for our weekly worship service filled with praise and a powerful message.",
            start_time=now + timedelta(days=2), end_time=now + timedelta(days=2, hours=2), location="Main Sanctuary, Downtown Campus", campus=c1
        )
        Event.objects.create(
            title="Youth Group Retreat", description="A weekend getaway for high school students to connect with God and each other.",
            start_time=now + timedelta(days=10), end_time=now + timedelta(days=12), location="Camp Hope", campus=c2
        )
        Event.objects.create(
            title="Community Food Drive", description="Help us pack boxes of food for families in need around our city.",
            start_time=now + timedelta(days=5), end_time=now + timedelta(days=5, hours=4), location="Northside Campus Parking Lot", campus=c2
        )
        Event.objects.create(
            title="Global Online Prayer Night", description="Connect from anywhere in the world to pray together as a unified body.",
            start_time=now + timedelta(days=4), end_time=now + timedelta(days=4, hours=1), location="Zoom Link", campus=c3
        )
        self.stdout.write("Created 4 Upcoming Events.")

        # 5. Create 3 Donation Campaigns
        Campaign.objects.all().delete()
        Campaign.objects.create(title="Building Fund", description="Help us expand the Downtown Campus sanctuary to make room for more.", goal_amount=500000, current_amount=150000)
        Campaign.objects.create(title="Missions Offering 2026", description="Supporting our global missionaries in over 10 countries.", goal_amount=100000, current_amount=45000)
        Campaign.objects.create(title="Youth Camp Scholarships", description="Ensure every student can attend summer camp regardless of financial ability.", goal_amount=15000, current_amount=8000)
        self.stdout.write("Created 3 Donation Campaigns.")

        # 6. Create 5 Prayer Requests
        PrayerRequest.objects.all().delete()
        PrayerRequest.objects.create(name="Sarah Jenkins", content="Please pray for my mother's upcoming surgery on Tuesday. She is very anxious.", is_public=True)
        PrayerRequest.objects.create(name="Anonymous", content="Praying for financial breakthrough after losing my job last month.", is_public=True)
        PrayerRequest.objects.create(name="Mark", content="My son is struggling with addiction. Please pray for his complete deliverance.", is_public=True)
        PrayerRequest.objects.create(name="The Thompson Family", content="Praise report! Our baby girl was born healthy and safe. Thank you for your prayers.", is_public=True, is_answered=True)
        PrayerRequest.objects.create(name="Jessica", content="Pray for guidance as I transition into a new career path.", is_public=True)
        self.stdout.write("Created 5 Prayer Requests.")

        # 7. Create 3 Ministry Groups
        GroupCategory.objects.all().delete()
        MinistryGroup.objects.all().delete()
        cat1 = GroupCategory.objects.create(name="Bible Study")
        cat2 = GroupCategory.objects.create(name="Support Group")
        cat3 = GroupCategory.objects.create(name="Youth Ministry")

        MinistryGroup.objects.create(
            name="Men's Wednesday Morning Study", description="A deep dive into Proverbs for men of all ages. Coffee provided!",
            category=cat1, campus=c1, meeting_schedule="Wednesdays at 6:30 AM", max_capacity=30
        )
        MinistryGroup.objects.create(
            name="GriefShare", description="A safe, welcoming place where people understand the difficult emotions of grief.",
            category=cat2, campus=c2, meeting_schedule="Thursdays at 7:00 PM", max_capacity=15
        )
        MinistryGroup.objects.create(
            name="High School Ministry", description="For students 9th-12th grade to grow in their faith.",
            category=cat3, campus=c1, meeting_schedule="Fridays at 6:30 PM", max_capacity=100
        )
        self.stdout.write("Created 3 Ministry Groups.")

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database!'))
