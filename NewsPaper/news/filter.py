# from django_filters import FilterSet, DateTimeFilter, CharFilter, ChoiceFilter
# from django.forms.widgets import DateTimeInput
# from .models import Post
# from .resources import POST_TYPE_CHOICES
#
#
# class NewsFilter(FilterSet):
#     class Meta:
#         model = Post
#         fields = ['categories', 'created_at']
#
#
# class PostFilter(FilterSet):
#     added_after = DateTimeFilter(
#         field_name='created_at',
#         lookup_expr='gt',
#         label='Добавлено после',
#         widget=DateTimeInput(
#             format='%d-%m-%Y',
#             attrs={'type': 'datetime-local'},
#         ),
#     )
#     title = CharFilter(
#         field_name='title',
#         lookup_expr='icontains',
#         label='Название содержит',
#     )
#
#
#     post_type = ChoiceFilter(
#         label='Категория поста',
#         empty_label='Выбери из списка',
#         choices=POST_TYPE_CHOICES,
#         field_name='post_type',
#         lookup_expr='exact',
#         method='filter'
#     )
#
#     def filter(self, queryset, name, value):
#         return queryset.filter(**{name: value})
#
#     class Meta:
#         model = Post
#         fields = ['added_after', 'title', 'categories', 'post_type']


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
# class PostFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     created_at = django_filters.NumberFilter(lookup_expr='gt')
#
#    class Meta:
#        # В Meta классе мы должны указать Django модель,
#        # в которой будем фильтровать записи.
#        model = Post
#        # В fields мы описываем по каким полям модели
#        # будет производиться фильтрация.
#        fields = {
#            # поиск по названию
#            'title': ['icontains'],
#            'categories': ['icontains'],
#            # количество товаров должно быть больше или равно
#            'created_at': ['gt'],
#        }


from django_filters import FilterSet, DateTimeFilter, CharFilter, ChoiceFilter
from django.forms.widgets import DateTimeInput
from .models import Post
from .resources import POST_TYPE_CHOICES


class NewsFilter(FilterSet):
    class Meta:
        model = Post
        fields = ['categories', 'created_at']


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='created_at',
        lookup_expr='gt',
        label='Добавлено после',
        widget=DateTimeInput(
            format='%d-%m-%Y',
            attrs={'type': 'datetime-local'},
        ),
    )
    title = CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Название содержит',
    )

    post_type = ChoiceFilter(
        label='Категория поста',
        empty_label='Выбери из списка',
        choices=[(choice[0], choice[1]) for choice in POST_TYPE_CHOICES],  # Используем значения из POST_TYPE_CHOICES
        field_name='post_type',
        lookup_expr='exact',
    )

    class Meta:
        model = Post
        fields = ['added_after', 'title', 'categories', 'post_type']
