from home import models


def load_categories(request):
	return {
		"categories": models.BlogCategory.objects.order_by('order').all(),
	}
