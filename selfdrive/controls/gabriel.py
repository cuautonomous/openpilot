import zmq
import selfdrive.messaging as messaging

gabriel = messaging.pub_sock(context, service_list['gabriel'].port)

def hacker_thread(gctx=None, rate=25):
  plan_send = messaging.new_message()
  plan_send.init('pathPlan')
  plan_send.gabriel.degrees = 21 #for example
  gabriel.send(plan_send.to_bytes())


def main(gctx=None):
  hacker_thread(gctx, 25)


if __name__ == "__main__":
  main()


