import ru_local

# Setting constants
START_DIST = 16637000000
VOYAGER_SPEED = 38241
# Conversion from meters per second to miles per hour.
SIGNAL_SPEED = 299792458 * 2.236936  

print(ru_local.START_MSG)

# Get number of days since the set date.
days = int(input(ru_local.INPUT_MSG))

ml_dist = START_DIST + 24 * days * VOYAGER_SPEED
km_dist = ml_dist * 1.61
astro_unit_dist = ml_dist * 1.07578 * 10**(-8)
signal_time = ml_dist / SIGNAL_SPEED

print('\n',
      ru_local.OUT_ML_DIST, ml_dist, '\n',
      ru_local.OUT_KM_DIST, km_dist, '\n',
      ru_local.OUT_ASTRO_UNIT_DIST, astro_unit_dist, '\n',
      ru_local.SIGNAL_TIME, signal_time)