import zmq
import selfdrive.messaging as messaging
from selfdrive.services import service_list
from common.realtime import Ratekeeper

context = zmq.Context()
gabriel = messaging.pub_sock(context, service_list['gabriel'].port)

def hacker_thread(gctx=None, rate=25):

  # start the loop
  rk = Ratekeeper(rate, print_delay_threshold=2. / 1000)

  while True:
    plan_send = messaging.new_message()
    plan_send.init('pathPlan')
    plan_send.pathPlan.angleSteers = 21 #for example
    gabriel.send(plan_send.to_bytes())

    rk.keep_time()  # Run at 25Hz


def main(gctx=None):
  hacker_thread(gctx, 25)


if __name__ == "__main__":
  main()
