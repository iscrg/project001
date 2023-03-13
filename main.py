import ru_local

# Setting constants
start_dist = 16637000000
voyager_speed = 38241
# Conversion from meters per second to miles per hour.
signal_speed = 299792458 * 2.236936  

print(ru_local.START_MSG)

# Get number of days since the set date.
days = int(input(ru_local.INPUT_MSG))

ml_dist = start_dist + 24 * days * voyager_speed
km_dist = ml_dist * 1.61
astro_unit_dist = ml_dist * 1.07578 * 10**(-8)
signal_time = ml_dist / signal_speed

print('\n',
      ru_local.OUT_ML_DIST, ml_dist, '\n',
      ru_local.OUT_KM_DIST, km_dist, '\n',
      ru_local.OUT_ASTRO_UNIT_DIST, astro_unit_dist, '\n',
      ru_local.SIGNAL_TIME, signal_time)