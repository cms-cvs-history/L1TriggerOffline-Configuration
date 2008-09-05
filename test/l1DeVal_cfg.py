import FWCore.ParameterSet.Config as cms

process = cms.Process("L1DEVAL")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu2008_2E30_cff")

process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")

process.load("Geometry.CMSCommonData.cmsSimIdealGeometryXML_cfi")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")

process.load("L1Trigger.Configuration.L1Emulator_cff")

process.load("L1Trigger.HardwareValidation.L1HardwareValidation_cff")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
process.p1 = cms.Path(process.L1HardwareValidation)
process.TFileService.fileName = 'l1DeVal.root'

