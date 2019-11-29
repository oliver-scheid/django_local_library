from django.contrib import admin

# Register your models here.

from catalog.models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)



class BookInline(admin.TabularInline):
    model = Book
    extra = 0

#Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

#Define the admin class and register it using the @register decorator
@admin.register(Book) 
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


#Define the admin Class and register it using the @admin.register decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )


#Define the admin Class and register it using the @admin.register decorator
#@admin.register(User)
#class UserAdmin(admin.ModelAdmin):
    #list_display = ('username', 'email_address', 'first_name', 'last_name', 'permissions', 'staff_status')