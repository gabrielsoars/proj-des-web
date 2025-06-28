from rest_framework.views import APIView
from rest_framework.response import Response
from api_clients.api_football import get_matches_today

class MatchesTodayView(APIView):
    def get(self, request):
        data = get_matches_today()
        return Response(data)
