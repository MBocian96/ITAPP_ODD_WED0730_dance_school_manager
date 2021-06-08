# from django_cron import CronJobBase, Schedule
#
# from authentication_module.models import set_absence_for_ongoing_courses
#
#
# class AbsanceCron(CronJobBase):
#     trigger_hours = (
#         '05:45', '06:45', '07:45', '08:45', '09:45',
#         '10:45', '11:45', '12:45', '13:45', '14:45',
#         '15:45', '16:45', '17:45', '18:45', '19:45',
#         '20:45', '21:45', '22:45', '23:45', '00:45',
#         '01:45', '02:45', '03:45', '04:45')
#     code = 'dance_school_manager.cron.AbsanceCron'
#
#     schedule = Schedule(run_every_mins=1)
#
#     def do(self):
#         print('Setting absences')
#         # set_absence_for_ongoing_courses(request=None)


def my_cron_job():
    print('Cron job is working')
