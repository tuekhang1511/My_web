def user_context_processor(request):
    if request.user.is_authenticated:
        return {'user': request.user}
    return {}