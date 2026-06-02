import jwt
from jwt import PyJWKClient

from mcp.server.auth.provider import TokenVerifier, AccessToken


USER_POOL_ID = "us-east-1_t8wytCttP"
REGION = "us-east-1"

ISSUER = (
    f"https://cognito-idp.{REGION}.amazonaws.com/{USER_POOL_ID}"
)

JWKS_URL = f"{ISSUER}/.well-known/jwks.json"


class CognitoTokenVerifier(TokenVerifier):

    def __init__(self):
        self.jwks_client = PyJWKClient(JWKS_URL)

    async def verify_token(self, token: str):

        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(token)

            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                issuer=ISSUER,
                options={
                    "verify_aud": False
                }
            )

            scopes = payload.get("scope", "").split()

            return AccessToken(
                token=token,
                client_id=payload["client_id"],
                scopes=scopes,
                expires_at=payload.get("exp"),
            )

        except Exception as e:
            print(f"JWT verification failed: {e}")
            return None
