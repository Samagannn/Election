from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, VoterViewSet, MyVotesViewSet, AppealListView, MyAppealListView

router = DefaultRouter()
router.register('candidates', CandidateViewSet)
router.register('votes', VoterViewSet)
router.register('myvotes', MyVotesViewSet)
router.register('appeal', AppealListView)
router.register('myappeal', MyAppealListView)

urlpatterns = [
    path('auth/', include('api.auth.urls')),
    path('', include(router.urls)),
]
