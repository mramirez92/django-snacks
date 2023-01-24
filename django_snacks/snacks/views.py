from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {"title": "Watermelon",
             "desc": "watermelon, it's juicy, sweet and refreshing!",
             "image": "https://images.unsplash.com/photo-1595475207225-428b62bda831?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1780&q=80"
             },
            {"title": "Flaming Hot Cheetos",
             "desc": "spicy",
             "image": "https://media.wired.com/photos/5927171e7034dc5f91bed9c2/191:100/w_1280,c_limit/RGB_Wired_FlamingHotCheetos_V1-B.jpg"
             },
            {"title": "Popcorn",
             "desc": "something",
             "image": "https://images.unsplash.com/photo-1589254513399-8ec9b4e8a831?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80",
             },
            {"title": "Cereal",
             "desc": "milk and cereal",
             "image": "https://images.unsplash.com/photo-1521483451569-e33803c0330c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1985&q=80"
             },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    # def get_context_data(self, **kwargs):
    #     context =super().get_context_data(**kwargs)
    #     context['aboutMe'] = [
    #         {},
    #         {},
    #     ]
    #     return context
