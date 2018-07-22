import GoogleFitness
import AppleHealthXmlParser
import sys

weightRecords = []
stepRecords = []
distanceRecords = []
heartRateRecords = []

records = AppleHealthXmlParser.parse(sys.argv[1]);

for record in records:
	if record.recordType == "HKQuantityTypeIdentifierBodyMass":
		weightRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierStepCount":
		stepRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierDistanceWalkingRunning":
		distanceRecords.append(record)
	if record.recordType == "HKQuantityTypeIdentifierHeartRate":
		heartRateRecords.append(record)

weightDataSource = GoogleFitness.createWeightDataSource()
stepDataSource = GoogleFitness.createStepDataSource()
distanceDataSource = GoogleFitness.createDistanceDataSource()
heartRateDataSource = GoogleFitness.createHeartRateDataSource()

if weightDataSource and len(weightRecords) > 0 :
	GoogleFitness.sendPoints(weightDataSource, weightRecords)

if stepDataSource and len(stepRecords) > 0 :
	GoogleFitness.sendPoints(stepDataSource, stepRecords)

if distanceDataSource and len(distanceRecords) > 0 :
	GoogleFitness.sendPoints(distanceDataSource, distanceRecords)







if heartRateDataSource and len(heartRateRecords) > 0 :
	GoogleFitness.sendPoints(heartRateDataSource, heartRateRecords)
