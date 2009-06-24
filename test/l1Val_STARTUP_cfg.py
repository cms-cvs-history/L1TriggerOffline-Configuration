import FWCore.ParameterSet.Config as cms

process = cms.Process("l1validation")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string("STARTUP_31X::All")

process.load("L1Trigger.Configuration.L1Extra_cff")
process.l1extraParticles.muonSource = cms.InputTag("hltGtDigis")
process.l1extraParticles.isolatedEmSource = cms.InputTag("hltGctDigis","isoEm")
process.l1extraParticles.nonIsolatedEmSource = cms.InputTag("hltGctDigis","nonIsoEm")
process.l1extraParticles.forwardJetSource = cms.InputTag("hltGctDigis","forJets")
process.l1extraParticles.centralJetSource = cms.InputTag("hltGctDigis","cenJets")
process.l1extraParticles.tauJetSource = cms.InputTag("hltGctDigis","tauJets")
process.l1extraParticles.etTotalSource = cms.InputTag("hltGctDigis")
process.l1extraParticles.etHadSource = cms.InputTag("hltGctDigis")
process.l1extraParticles.etMissSource = cms.InputTag("hltGctDigis")

process.load("L1TriggerOffline.L1Analyzer.L1MuonMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1EmMCAnalysis_cff")
process.load("L1TriggerOffline.L1Analyzer.L1IsoEmMCAnalysis_cff")
process.load("L1TriggerOffline.L1Analyzer.L1NonIsoEmMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1JetMCAnalysis_cff")
process.load("L1TriggerOffline.L1Analyzer.L1CenJetMCAnalysis_cff")
process.load("L1TriggerOffline.L1Analyzer.L1ForJetMCAnalysis_cff")
process.load("L1TriggerOffline.L1Analyzer.L1TauJetMCAnalysis_cff")

process.load("L1TriggerOffline.L1Analyzer.L1MetMCAnalysis_cff")

#process.load("L1TriggerOffline.L1Analyzer.L1IsoEmRecoAnalysis_cff")
#process.load("L1TriggerOffline.L1Analyzer.L1NonIsoEmRecoAnalysis_cff")


process.load("L1Trigger.GlobalTriggerAnalyzer.l1GtTrigReport_cfi")
process.l1GtTrigReport.L1GtRecordInputTag = cms.InputTag("hltGtDigis")

process.p = cms.Path(
                     process.L1MuonMCAnalysis
                     +process.L1EmMCAnalysis
                     +process.L1IsoEmMCAnalysis
                     +process.L1NonIsoEmMCAnalysis
                     +process.L1JetMCAnalysis
                     +process.L1CenJetMCAnalysis
                     +process.L1ForJetMCAnalysis
                     +process.L1TauJetMCAnalysis
                     +process.L1MetMCAnalysis)

process.e = cms.EndPath(process.l1GtTrigReport)
process.TFileService.fileName = 'l1Val.root'

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:TTbar_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

