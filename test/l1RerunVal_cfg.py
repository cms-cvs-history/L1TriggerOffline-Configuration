import FWCore.ParameterSet.Config as cms

process = cms.Process("L1VAL")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "STARTUP_V7::All"

process.load("L1Trigger.Configuration.SimL1Emulator_cff")
process.load("L1Trigger.Configuration.L1Extra_cff")
process.l1extraParticles.muonSource = cms.InputTag("simGmtDigis")
process.l1extraParticles.isolatedEmSource = cms.InputTag("simGctDigis","isoEm")
process.l1extraParticles.nonIsolatedEmSource = cms.InputTag("simGctDigis","nonIsoEm")
process.l1extraParticles.forwardJetSource = cms.InputTag("simGctDigis","forJets")
process.l1extraParticles.centralJetSource = cms.InputTag("simGctDigis","cenJets")
process.l1extraParticles.tauJetSource = cms.InputTag("simGctDigis","tauJets")
process.l1extraParticles.etMissSource = cms.InputTag("simGctDigis")
process.l1extraParticles.etTotalSource = cms.InputTag("simGctDigis")
process.l1extraParticles.etHadSource = cms.InputTag("simGctDigis")

process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.lumi1030.L1Menu_2008MC_2E30_Unprescaled_cff")

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
    fileNames = cms.untracked.vstring('')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)
process.p1 = cms.Path(process.SimL1Emulator
                      *process.L1Extra
                      *process.L1MuonMCAnalysis
                      +process.L1IsoEmMCAnalysis
                      +process.L1NonIsoEmMCAnalysis
                      +process.L1CenJetMCAnalysis
                      +process.L1ForJetMCAnalysis
                      +process.L1TauJetMCAnalysis
                      +process.L1MetMCAnalysis)

process.e = cms.EndPath(process.l1GtTrigReport)
process.TFileService.fileName = 'l1RerunVal.root'
process.l1GtTrigReport.L1GtRecordInputTag = 'simGtDigis'

