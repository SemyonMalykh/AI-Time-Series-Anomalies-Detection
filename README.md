# Time Series Anomaly Detection Challenge
[Link to the original challenge](https://compete.hexagon-ml.com/practice/competition/39/#description).

## Phase 1
You get access to a sample of 25 time series (10% of the data) as well as an evaluation script with the necessary data to do so.

- **phase_1**: contains files with one time series each. The filenames follow the strucure *id*\_UCR\_Anomaly\_*EndOfTrainingIndex*, where *EndOfTrainingIndex* is the final step for which no anomaly occurs. Afterwards, there is exactly one anomaly to find.
- **eval.py**: Evaluation script
- **metadata.csv**: contains additional data for every time series (like the anomaly places). You should not use this information during this phase.
- **example_submission**: an example to use with eval.py

## Phase 2
You will receive more data during this phase.