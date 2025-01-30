

def detect_ios(request):
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    is_ios = 'iphone' in user_agent or 'ipad' in user_agent
    return {'is_ios': is_ios}