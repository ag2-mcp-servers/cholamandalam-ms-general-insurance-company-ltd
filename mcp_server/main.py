# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:55:42+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    CripcCertificatePostRequest,
    CripcCertificatePostResponse,
    CripcCertificatePostResponse1,
    CripcCertificatePostResponse2,
    CripcCertificatePostResponse3,
    CripcCertificatePostResponse4,
    CripcCertificatePostResponse5,
    CripcCertificatePostResponse6,
    TwipcCertificatePostRequest,
    TwipcCertificatePostResponse,
    TwipcCertificatePostResponse1,
    TwipcCertificatePostResponse2,
    TwipcCertificatePostResponse3,
    TwipcCertificatePostResponse4,
    TwipcCertificatePostResponse5,
    TwipcCertificatePostResponse6,
)

app = MCPProxy(
    description='APIs provided by Cholamandalam MS General Insurance Company Ltd..',
    termsOfService='https://apisetu.gov.in/terms.php',
    title='Cholamandalam MS General Insurance Company Ltd.',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/cholainsurance/v3'}],
)


@app.post(
    '/cripc/certificate',
    description=""" API to verify Insurance Policy - Car. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def cripc(body: CripcCertificatePostRequest = None):
    """
    Insurance Policy - Car
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/twipc/certificate',
    description=""" API to verify Insurance Policy - Two Wheeler. """,
    tags=['insurance_policy_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def twipc(body: TwipcCertificatePostRequest = None):
    """
    Insurance Policy - Two Wheeler
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
