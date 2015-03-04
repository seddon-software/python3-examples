from pylons import session

class Nav():
    def __init__(self):
        self.page = 0
    
    def next(self):
        if 'page' in session:
            self.page = session['page']
        self.page += 1
        self.page %= 3
        session['page'] = self.page
        session.save()
        return self.page

