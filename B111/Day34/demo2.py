from abc import ABC,abstractmethod
class Remote(ABC):
    @abstractmethod
    def turn_on_off(self):
        pass


class LGTV(Remote):
    status='off'
    def turn_on_off(self):
        if  LGTV.status=='off':
            LGTV.status='on'
            print('TV was off, now turned ON')
        else:
            LGTV.status = 'off'
            print('TV was ON, now turned OFF')

class SONYTV(Remote):
    status='off'
    def turn_on_off(self):
        if  SONYTV.status=='off':
            SONYTV.status='on'
            print('TV was off, now turned ON')
        else:
            SONYTV.status = 'off'
            print('TV was ON, now turned OFF')

myTV=LGTV()
myTV.turn_on_off()
myTV.turn_on_off()

myTV2=SONYTV()
myTV2.turn_on_off()
myTV2.turn_on_off()