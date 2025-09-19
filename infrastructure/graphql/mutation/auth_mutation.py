import graphene
from application.use_cases.auth.login_service import AuthService
from graphql import GraphQLError

class LoginMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    user_id = graphene.Int()
    token = graphene.String()
    error = graphene.String()

    def mutate(self, info, username, password):
        try:
            result = AuthService.login(username, password)
            
            # Si hubo un error de autenticación
            if not result.get("success"):
                return LoginMutation(
                    success=False,
                    user_id=None,
                    token=None,
                    error=result.get("error", "Error desconocido")
                )

            # Retornamos usuario autenticado y token
            return LoginMutation(
                success=True,
                user_id=result.get("user_id"),
                token=result.get("token"),
                error=None
            )

        except Exception as e:
            # Capturamos cualquier error inesperado
            return LoginMutation(
                success=False,
                user_id=None,
                token=None,
                error=str(e)
            )
