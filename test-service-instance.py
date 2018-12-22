import argparse
import requests
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth

AWS_SERVICE = "execute-api"
AWS_REGION = "us-east-1"


def get_auth():
    return BotoAWSRequestsAuth(aws_host=host_name, aws_service=AWS_SERVICE, aws_region=AWS_REGION)


def test_service_health():
    url = "https://" + "/".join([host_name, "service", "health"])
    print "test starting for /service/health:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /service/health:GET"


def test_failed_admin_health():
    url = "https://" + "/".join([host_name, "admin", "health"])
    print "test starting for /admin/health:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /admin/health:GET"

    url = "https://" + "/".join([host_name, "scanner", "health"])
    print "\ntest starting for /scanner/health:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /scanner/health:GET"

    url = "https://" + "/".join([host_name, "gateway", "health"])
    print "\ntest starting for /gateway/health:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /gateway/health:GET"


#/service/gateways/<string:instance_or_ref_id>
def test_1():
    url = "https://" + "/".join([host_name, "service", "gateways", gw_id])
    print "test starting for /service/gateways/<string:instance_or_ref_id>:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /service/gateways/<string:instance_or_ref_id>:GET"


#/service/gateways/<string:instance_or_ref_id>/{gw_id}/endpoints
def test_2():
    url = "https://" + "/".join([host_name, "service", "gateways", gw_id, "endpoints"])
    print "test starting for /service/gateways/<string:instance_or_ref_id>/endpoints:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /service/gateways/<string:instance_or_ref_id>/endpoints:GET"


#/service/gateways/<string:instance_or_ref_id>/{gw_id}/endpoints/{ep_token}
def test_3():
    url = "https://" + "/".join([host_name, "service", "gateways", gw_id, "endpoints", ep_token])
    print "test starting for /service/gateways/<string:instance_or_ref_id>/endpoints/{ep_token}:GET"
    response = requests.get(url, auth=get_auth())
    print "response : %s" % response.json()
    print "test completed for /service/gateways/<string:instance_or_ref_id>/endpoints/{ep_token}:GET"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Veracode Test')

    parser.add_argument('--host_name', action="store", dest="host_name", default=None, help="host_name")

    parser.add_argument('--test_1', action="store_true", dest="test_1", default=False,
                        help="test_1 /service/gateways/{id}:GET")

    parser.add_argument('--test_2', action="store_true", dest="test_2", default=False,
                        help="test_2 /service/gateways/{id}/endpoints:GET")

    parser.add_argument('--test_3', action="store_true", dest="test_3", default=False,
                        help="test_3 /service/gateways/{id}/endpoints/{token}:GET")

    parser.add_argument('--test_fail', action="store_true", dest="test_fail", default=False,
                        help="test_fail /admin/health:GET")

    parser.add_argument('--gw_id', action="store", dest="gw_id", default=None, help="gw_id")
    parser.add_argument('--ep_token', action="store", dest="ep_token", default=None, help="ep_token")

    args = parser.parse_args()

    host_name = args.host_name

    if host_name is None:
        exit("host_name is empty")
    else:
        if args.test_1:
            gw_id = args.gw_id

            if gw_id is None:
                exit("gw_id is empty")
            else:
                test_1()
        elif args.test_2:
            gw_id = args.gw_id

            if gw_id is None:
                exit("gw_id is empty")
            else:
                test_2()
        elif args.test_3:
            gw_id = args.gw_id
            ep_token = args.ep_token

            if gw_id is None:
                exit("gw_id is empty")
            if ep_token is None:
                exit("ep_token is empty")
            else:
                test_3()
        elif args.test_fail:
            test_failed_admin_health()
        else:
            test_service_health()
