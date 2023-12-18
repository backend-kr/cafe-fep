class AdapterMixin(object):
    adapter = None
    response_serializer_class = None
    base_url = None
    endpoint = ''
    kwargs = {}

    def to_representation(self, instance):
        if self.adapter:
            response = self.get_adapter_response(endpoint=self.endpoint, body=instance)
            serializer = self.response_serializer_class(response)
        return serializer.data

    def get_adapter_response(self, endpoint, body):
        response = self.adapter.request(additional_url=endpoint,
                                        body=body,
                                        **self.kwargs)
        return response


class MappingViewSetMixin(object):
    serializer_action_map = {}
    permission_classes_map = {}
    queryset_map = {}

    def get_queryset(self):
        return self.queryset_map.get(self.action, self.queryset)

    def get_permissions(self):
        permission_classes = self.permission_classes
        if self.permission_classes_map.get(self.action, None):
            permission_classes = self.permission_classes_map[self.action]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.serializer_action_map.get(self.action, None):
            return self.serializer_action_map[self.action]
        return self.serializer_class