from django.core.management.base import BaseCommand
from faculty.models import Registration
from django.db.models import Count

class Command(BaseCommand):
    help = 'Remove duplicate registrations'

    def handle(self, *args, **kwargs):
        duplicates = (
            Registration.objects
            .values('student_id', 'course_id')
            .annotate(count=Count('id'))
            .filter(count__gt=1)
        )

        for duplicate in duplicates:
            # Get all duplicate records
            dup_records = Registration.objects.filter(student_id=duplicate['student_id'], course_id=duplicate['course_id'])
            
            # Keep one and delete the rest
            dup_records.exclude(id=dup_records.first().id).delete()

        self.stdout.write(self.style.SUCCESS('Duplicate registrations removed successfully.'))
