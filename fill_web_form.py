# fill_web_form.py
import mechanize


def fill_form(url, form, form_name, data):
        print "opening browser"
        br = mechanize.Browser()
        print "opening url...please wait"
        br.open(url)
        print br.title()
        print "selecting form"
        br.select_form(name=form)
        print "entering string:'" + data +"' into form"
        br[form_name] = data
        print "submitting form"
        br.submit()


