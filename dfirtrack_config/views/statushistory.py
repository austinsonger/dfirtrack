from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from dfirtrack_artifacts.models import Artifact, Artifactpriority, Artifactstatus
from dfirtrack_config.models import Statushistory, StatushistoryEntry
from dfirtrack_main.models import Analysisstatus, System, Systemstatus, Task, Taskpriority, Taskstatus


def statushistory_save_objects():

    # create empty statushistory (just contains primary key and datetime field)
    statushistory = Statushistory.objects.create()

    """ save numbers of current artifacts, systems and tasks """

    # save number of artifacts (statushistoryentry_model_key not necessary)
    artifacts_number = Artifact.objects.all().count()
    StatushistoryEntry.objects.create(
        statushistory = statushistory,
        statushistoryentry_model_name = 'artifacts_number',
        statushistoryentry_model_value = artifacts_number,
    )

    # save number of systems (statushistoryentry_model_key not necessary)
    systems_number = System.objects.all().count()
    StatushistoryEntry.objects.create(
        statushistory = statushistory,
        statushistoryentry_model_name = 'systems_number',
        statushistoryentry_model_value = systems_number,
    )

    # save number of tasks (statushistoryentry_model_key not necessary)
    tasks_number = Task.objects.all().count()
    StatushistoryEntry.objects.create(
        statushistory = statushistory,
        statushistoryentry_model_name = 'tasks_number',
        statushistoryentry_model_value = tasks_number,
    )

    """ save analysisstatus """

    # get all objects
    analysisstatus_all = Analysisstatus.objects.all().order_by('analysisstatus_name')
    # loop over objects
    for analysisstatus in analysisstatus_all:
        # count number of associated objects
        systems_number_analysisstatus = System.objects.filter(analysisstatus=analysisstatus).count()
        # save single object in history including its name and number of associated objects
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'analysisstatus',
            statushistoryentry_model_key = analysisstatus.analysisstatus_name,
            statushistoryentry_model_value = systems_number_analysisstatus,
        )

    """ save artifactpriority """

    # get all objects
    artifactpriority_all = Artifactpriority.objects.all().order_by('artifactpriority_name')
    # loop over objects
    for artifactpriority in artifactpriority_all:
        # count number of associated objects
        artifacts_number_artifactpriority = Artifact.objects.filter(artifactpriority=artifactpriority).count()
        # save single object in history including its name and number of associated objects
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'artifactpriority',
            statushistoryentry_model_key = artifactpriority.artifactpriority_name,
            statushistoryentry_model_value = artifacts_number_artifactpriority,
        )

    """ save artifactstatus """

    # get all objects
    artifactstatus_all = Artifactstatus.objects.all().order_by('artifactstatus_name')
    # loop over objects
    for artifactstatus in artifactstatus_all:
        # count number of associated objects
        artifacts_number_artifactstatus = Artifact.objects.filter(artifactstatus=artifactstatus).count()
        # save single object in history including its name and number of associated objects
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'artifactstatus',
            statushistoryentry_model_key = artifactstatus.artifactstatus_name,
            statushistoryentry_model_value = artifacts_number_artifactstatus,
        )

    """ save systemstatus """

    # get all objects
    systemstatus_all = Systemstatus.objects.all().order_by('systemstatus_name')
    # loop over objects
    for systemstatus in systemstatus_all:
        # count number of associated objects
        systems_number_systemstatus = System.objects.filter(systemstatus=systemstatus).count()
        # save single object in history including its name and number of associated objects
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'systemstatus',
            statushistoryentry_model_key = systemstatus.systemstatus_name,
            statushistoryentry_model_value = systems_number_systemstatus,
        )

    """ save taskstatus """

    # get all objects
    taskstatus_all = Taskstatus.objects.all().order_by('taskstatus_name')
    # loop over objects
    for taskstatus in taskstatus_all:
        # count number of associated objects
        systems_number_taskstatus = Task.objects.filter(taskstatus=taskstatus).count()
        # save single object in history including its name and number of associated objects
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'taskstatus',
            statushistoryentry_model_key = taskstatus.taskstatus_name,
            statushistoryentry_model_value = systems_number_taskstatus,
        )

    """ save taskpriority """

    # get all objects
    taskpriority_all = Taskpriority.objects.all().order_by('taskpriority_name')
    # loop over objects
    for taskpriority in taskpriority_all:
        # count number of associated objects
        systems_number_taskpriority = Task.objects.filter(taskpriority=taskpriority).count()
        # save single object in history including its name and number of associated objects
        StatushistoryEntry.objects.create(
            statushistory = statushistory,
            statushistoryentry_model_name = 'taskpriority',
            statushistoryentry_model_key = taskpriority.taskpriority_name,
            statushistoryentry_model_value = systems_number_taskpriority,
        )

    return

@login_required(login_url="/login")
def statushistory_save(request):

    statushistory_save_objects()

    # create message
    messages.success(request, 'Statushistory saved')

    # reload page to show message
    return redirect(reverse('status'))

def statushistory_save_cron():

    statushistory_save_objects()

    # reload page to show message
    return redirect(reverse('status'))
