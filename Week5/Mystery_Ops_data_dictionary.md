# Mystery_Ops Data Dictionary

`Mystery_Ops.csv` supports Lab5: The Nairobi Bottleneck Investigation.

Rows are daily depot-shift operational records for 2026. The primary KPI is `throughput_barrels`.

## Columns

- `record_id`: Unique row identifier.
- `operation_date`: Date stored as `DD/MM/YYYY` text so students must parse it.
- `depot`: Operating location: Nairobi, Mombasa, Kisumu, or Eldoret.
- `shift`: Day or Night operational shift.
- `operator_id`: Operator assigned to the shift. Some values are missing.
- `machine_id`: Pump or machine used during the shift.
- `throughput_barrels`: Daily shift throughput KPI. Some values are missing due to a simulated export gap.
- `temperature_c`: Ambient temperature. Includes a systematic Nairobi sensor outage.
- `maintenance_flag`: Binary indicator for records requiring maintenance investigation.
- `voltage_count`: Integer SCADA voltage count; intentionally discrete.
- `incident_type`: Normal, missed maintenance, operator blunder, or brief equipment fault.

## Built-In Mystery

Nairobi experiences a structural throughput break starting on 01/02/2026. The dominant root cause is pump `NBI-P03`, where missed maintenance drives an approximate 40% throughput loss. Other depots have normal variation plus occasional isolated outliers, so Pareto and drill-down analysis should isolate Nairobi as the main contributor to the loss.
