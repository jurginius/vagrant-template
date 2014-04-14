from easy_pdf.views import PDFTemplateView

class DestinationPDFView(PDFTemplateView):
    template_name = "pdfmaker/destination.html"

    def get_context_data(self, **kwargs):
        return super(DestinationPDFView, self).get_context_data(
            pagessize="A4",
            title="Hi There!",
            **kwargs
        )
