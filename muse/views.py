from .models import Section
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SectionSerializer

class ListSectionView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'section_index.html'
    serializer_class = SectionSerializer

    def get(self, request, *args, **kwargs):
        queryset = Section.objects.all()
        return Response({'Sections': queryset})

class ListSectionDetailView(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'section_detail.html'
    serializer_class = SectionSerializer

    def get(self, request, pk):
        queryset_1 = Section.objects.get(pk=pk)
        queryset_2 = Section.objects.all()
        
        if pk == 1:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='section_detail.html')
        elif pk == 2:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='section_detail.html')
        elif pk == 3:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='section_detail.html')
        elif pk == 4:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='methods.html')
        elif pk == 5:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='results.html')
        elif pk == 6:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='section_detail.html')
        elif pk == 7:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='section_detail.html')
        elif pk == 8:
            return Response({'Section': queryset_1, 'Sections': queryset_2}, template_name='acknowledgements.html')
             


