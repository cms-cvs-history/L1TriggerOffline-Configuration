import FWCore.ParameterSet.Config as cms

process = cms.Process("l1validation")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("L1Trigger.Configuration.L1DummyConfig_cff")

process.load("L1Trigger.Configuration.L1Extra_cff")

process.load("L1TriggerOffline.L1Analyzer.L1MuonMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1IsoEmMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1NonIsoEmMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1IsoEmRecoAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1NonIsoEmRecoAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1CenJetMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1TauJetMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1ForJetMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1MetMCAnalysis_cff")

process.load("L1Trigger.GlobalTriggerAnalyzer.l1GtTrigReport_cfi")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:E_35_ALL.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
process.p = cms.Path(process.L1MuonMCAnalysis+process.L1IsoEmMCAnalysis+process.L1NonIsoEmMCAnalysis+process.L1CenJetMCAnalysis+process.L1ForJetMCAnalysis+process.L1TauJetMCAnalysis+process.L1MetMCAnalysis)
process.e = cms.EndPath(process.l1GtTrigReport)
process.TFileService.fileName = 'l1validation.root'

