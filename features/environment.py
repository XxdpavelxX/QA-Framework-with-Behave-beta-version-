from selenium import webdriver
import os
import shutil
import time
import HTMLTestRunner



def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    context.browser = webdriver.Chrome()
    print("Before scenario\n")


def after_scenario(context, scenario):

    reportFile = '/Users/edvorkin/python_behave_template-master' + '/Output+'+'.html'
    reportName =  'Output' +'.html'
    print ('report file: ', reportFile)
    fp = file(reportFile,'wb')
    #suite = unittest.TestSuite()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report for Build ',description='This testcase was executed in Env: '+' Pub: '+' Build:')

    #result = runner.run(suite)

    print("scenario status" + scenario.status)


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.browser.save_screenshot(scenario.name + "_failed.png")

    context.browser.quit()
    print("After scenario\n")

def after_feature(context,feature):
     print("\nAfter feature")

def after_all(context):

    print ("User data:", context.config.userdata, "hi", context.config.userdata.keys())
    print ("Environ: ", os.environ.keys())
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in os.environ.keys():
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        if os.environ['ARCHIVE'] == "Yes":
            shutil.make_archive(
    time.strftime("%d_%m_%Y"),"zip",
     "failed_scenarios_screenshots")
            #os.rmdir("failed_scenarios_screenshots")
            print("Executing after all")
'''test'''