from django.db import models

# Create your models here.
class RideFile(models.Model):
    file = models.FileField(upload_to='activities/%Y/%m/%d')

class Activity(models.Model):
    fitfile = models.OneToOneField(RideFile, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    start_time = models.DateTimeField()
    start_position_lat = models.FloatField(default=None, blank=True, null=True)
    start_position_long = models.FloatField(default=None, blank=True, null=True)
    total_elapsed_time = models.FloatField(default=None, blank=True, null=True)
    total_timer_time = models.FloatField(default=None, blank=True, null=True)
    total_distance = models.FloatField(default=None, blank=True, null=True)
    total_cycles = models.IntegerField(default=None, blank=True, null=True)
    total_work = models.IntegerField(default=None, blank=True, null=True)
    enhanced_avg_speed = models.IntegerField(default=None, blank=True, null=True)
    enhanced_max_speed = models.IntegerField(default=None, blank=True, null=True)
    enhanced_avg_altitude = models.IntegerField(default=None, blank=True, null=True)
    enhanced_min_altitude = models.IntegerField(default=None, blank=True, null=True)
    enhanced_max_altitude = models.IntegerField(default=None, blank=True, null=True)
    total_calories = models.IntegerField(default=None, blank=True, null=True)
    avg_speed = models.IntegerField(default=None, blank=True, null=True)
    max_speed = models.IntegerField(default=None, blank=True, null=True)
    avg_power = models.IntegerField(default=None, blank=True, null=True)
    max_power = models.IntegerField(default=None, blank=True, null=True)
    total_ascent = models.IntegerField(default=None, blank=True, null=True)
    total_descent = models.IntegerField(default=None, blank=True, null=True)
    num_laps = models.IntegerField(default=None, blank=True, null=True)
    normalized_power = models.IntegerField(default=None, blank=True, null=True)
    training_stress_score = models.FloatField(default=None, blank=True, null=True)
    intensity_factor = models.FloatField(default=None, blank=True, null=True)
    threshold_power = models.IntegerField(default=None, blank=True, null=True)
    event = models.CharField(max_length=10, default=None, blank=True, null=True)
    event_type = models.CharField(max_length=10, default=None, blank=True, null=True)
    sport = models.CharField(max_length=20, default=None, blank=True, null=True)
    sub_sport = models.CharField(max_length=10, default=None, blank=True, null=True)
    avg_heart_rate = models.IntegerField(default=None, blank=True, null=True)
    max_heart_rate = models.IntegerField(default=None, blank=True, null=True)
    avg_cadence = models.IntegerField(default=None, blank=True, null=True)
    max_cadence = models.IntegerField(default=None, blank=True, null=True)
    total_training_effect = models.FloatField(default=None, blank=True, null=True)
    avg_temperature = models.IntegerField(default=None, blank=True, null=True)
    max_temperature = models.IntegerField(default=None, blank=True, null=True)
    avg_fractional_cadence = models.FloatField(default=None, blank=True, null=True)
    max_fractional_cadence = models.FloatField(default=None, blank=True, null=True)
    total_fractional_cycles = models.FloatField(default=None, blank=True, null=True)
    total_anaerobic_training_effect = models.FloatField(default=None, blank=True, null=True)
    # nec_lat = models.FloatField(default=None, blank=True, null=True)
    # nec_long = models.FloatField(default=None, blank=True, null=True)
    # swc_lat = models.FloatField(default=None, blank=True, null=True)
    # swc_long = models.FloatField(default=None, blank=True, null=True)
    # avg_stroke_count = models.IntegerField(default=None, blank=True, null=True)
    # time_standing = models.IntegerField(default=None, blank=True, null=True)
    # message_index = models.IntegerField(default=None, blank=True, null=True)
    # first_lap_index = models.IntegerField(default=None, blank=True, null=True)
    # left_right_balance = models.IntegerField(default=None, blank=True, null=True)
    # avg_stroke_distance = models.IntegerField(default=None, blank=True, null=True)
    # pool_length = models.IntegerField(default=None, blank=True, null=True)
    # num_active_lengths = models.IntegerField(default=None, blank=True, null=True)
    # avg_vertical_oscillation = models.IntegerField(default=None, blank=True, null=True)
    # avg_stance_time_percent = models.IntegerField(default=None, blank=True, null=True)
    # avg_stance_time = models.IntegerField(default=None, blank=True, null=True)
    # stand_count = models.IntegerField(default=None, blank=True, null=True)
    # avg_vertical_ratio = models.IntegerField(default=None, blank=True, null=True)
    # avg_stance_time_balance = models.IntegerField(default=None, blank=True, null=True)
    # avg_step_length = models.IntegerField(default=None, blank=True, null=True)
    # event_group = models.IntegerField(default=None, blank=True, null=True)
    # trigger = models.CharField(max_length=20, default=None, blank=True, null=True)
    # swim_stroke = models.IntegerField(default=None, blank=True, null=True)
    # pool_length_unit = models.IntegerField(default=None, blank=True, null=True)
    # avg_left_torque_effectiveness = models.IntegerField(default=None, blank=True, null=True)
    # avg_right_torque_effectiveness = models.IntegerField(default=None, blank=True, null=True)
    # avg_left_pedal_smoothness = models.IntegerField(default=None, blank=True, null=True)
    # avg_right_pedal_smoothness = models.IntegerField(default=None, blank=True, null=True)
    # avg_combined_pedal_smoothness = models.IntegerField(default=None, blank=True, null=True)
    # avg_left_pco = models.IntegerField(default=None, blank=True, null=True)
    # avg_right_pco = models.IntegerField(default=None, blank=True, null=True)
    # avg_cadence_position = models.IntegerField(default=None, blank=True, null=True)
    # max_cadence_position = models.IntegerField(default=None, blank=True, null=True)


class Device(models.Model):
    serial_number = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=30)
    garmin_product = models.CharField(max_length=30)

class Record(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    position_lat = models.FloatField(default=None, blank=True, null=True)
    position_long = models.FloatField(default=None, blank=True, null=True)
    distance = models.FloatField(default=None, blank=True, null=True)
    accumulated_power = models.IntegerField(default=None, blank=True, null=True)
    speed = models.FloatField(default=None, blank=True, null=True)
    altitude = models.FloatField(default=None, blank=True, null=True)
    power = models.IntegerField(default=None, blank=True, null=True)
    heart_rate = models.IntegerField(default=None, blank=True, null=True)
    cadence = models.IntegerField(default=None, blank=True, null=True)
    temperature = models.IntegerField(default=None, blank=True, null=True)
