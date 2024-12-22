from django.core.management.base import BaseCommand, CommandError
from books.models import Book, Category, Subcategory
from tablib import Dataset


class Command(BaseCommand):
    help = "Import all Books from the csv file"

    #def add_arguments(self, parser):
    
    #    parser.add_argument("poll_ids", nargs="+", type=int)

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('This command works')
        )
        with open('data_test.csv', 'r') as fh:
            imported_data = Dataset().load(fh)

        self.stdout.write(str(imported_data.headers))
        categories = list(set(imported_data['Category']))   
        self.stdout.write(str(categories))
        for item in imported_data.dict:
            category_obj, category_created = Category.objects.get_or_create(name=item["Category"])
            subcategory_obj, subcategory_created = Subcategory.objects.get_or_create(
                category=category_obj, 
                name=item["SubCategory"])
            book_obj = Book.objects.get_or_create(
                num=item["Num"], 
                title=item["Name"], 
                author=item["Author"], 
                category=category_obj,
                subcategory=subcategory_obj,
                year=item["Year"],
                tom=item["Tom"],
                publisher=item["Publisher"],
                notes=item["Notes"])

            
            self.stdout.write(str(category_obj))
            self.stdout.write(str(subcategory_obj))
            self.stdout.write(str(book_obj))
        # for poll_id in options["poll_ids"]:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(
        #         self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
        #     )