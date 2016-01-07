from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status


class WebAPIView(APIView):
    authentication_classes = (authentication.SessionAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    # Get only one object by its ID or PK
    def get(self, request, pk, environment, format=None):
        environment.load_data('get', pk=pk)
        if len(environment.permissions) == 0 or request.user.has_perms(environment.permissions):
            serial = environment.serializer(environment.query, many=False, read_only=True)
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    # Get the list of objects
    def patch(self, request, environment, format=None):
        environment.load_data(method='patch', filters=request.data.dict())
        if len(environment.permissions) == 0 or request.user.has_perms(environment.permissions):
            serial = environment.serializer(environment.query, many=True, read_only=True)
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    # Create a new object from scratch
    def post(self, request, environment, format=None):
        environment.load_data('post')
        if len(environment.permissions) == 0 or request.user.has_perms(environment.permissions):
            serial = environment.serializer(request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.errors, status=status.HTTP_412_PRECONDITION_FAILED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    # Update an existing object using its ID or PK
    def put(self, request, pk, environment, format=None):
        environment.load_data('put', pk=pk)
        if len(environment.permissions) == 0 or request.user.has_perms(environment.permissions):
            serial = environment.serializer(environment.query, data=request.data)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_202_ACCEPTED)
            return Response(serial.errors, status=status.HTTP_412_PRECONDITION_FAILED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    # Delete an object by using its ID or PK
    def delete(self, request, pk, environment, format=None):
        environment.load_data('delete', pk=pk)
        if len(environment.permissions) == 0 or request.user.has_perms(environment.permissions):
            environment.query.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
