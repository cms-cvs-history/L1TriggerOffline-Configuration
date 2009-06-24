import FWCore.ParameterSet.Config as cms

process = cms.Process("L1VAL")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/MixingNoPileUp_cff')
process.load('Configuration/StandardSequences/GeometryIdeal_cff')
process.load('Configuration/StandardSequences/MagneticField_38T_cff')
process.load('Configuration/StandardSequences/Generator_cff')
process.load('Configuration/StandardSequences/VtxSmearedEarly10TeVCollision_cff')

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "STARTUP_31X::All"

#process.load("L1TriggerConfig.L1ScalesProducers.L1CaloInputScalesConfig_cff")

#from CondTools.L1Trigger.L1CondDBSource_cff import initCondDBSource
#initCondDBSource( process,
#                inputDBConnect = 'sqlite_file:/afs/cern.ch/user/w/wsun/public/conddb/l1config31XStartupV10.db',
#                tagBase = 'STARTUP',
#                includeAllTags = True )

process.load('Configuration/StandardSequences/Digi_cff')

process.load("L1Trigger.Configuration.SimL1Emulator_cff")
import L1Trigger.Configuration.L1Extra_cff
process.hltL1extraParticles = L1Trigger.Configuration.L1Extra_cff.l1extraParticles.clone()
process.hltL1extraParticles.muonSource = cms.InputTag("simGmtDigis")
process.hltL1extraParticles.isolatedEmSource = cms.InputTag("simGctDigis","isoEm")
process.hltL1extraParticles.nonIsolatedEmSource = cms.InputTag("simGctDigis","nonIsoEm")
process.hltL1extraParticles.forwardJetSource = cms.InputTag("simGctDigis","forJets")
process.hltL1extraParticles.centralJetSource = cms.InputTag("simGctDigis","cenJets")
process.hltL1extraParticles.tauJetSource = cms.InputTag("simGctDigis","tauJets")
process.hltL1extraParticles.etMissSource = cms.InputTag("simGctDigis")
process.hltL1extraParticles.etTotalSource = cms.InputTag("simGctDigis")
process.hltL1extraParticles.htMissSource = cms.InputTag("simGctDigis")
process.hltL1extraParticles.etHadSource = cms.InputTag("simGctDigis")
process.hltL1extraParticles.hfRingEtSumsSource = cms.InputTag("simGctDigis")
process.hltL1extraParticles.hfRingBitCountsSource = cms.InputTag("simGctDigis")

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
process.l1GtTrigReport.L1GtRecordInputTag = cms.InputTag("simGtDigis")

process.p = cms.Path(process.pdigi
                     +process.SimL1Emulator
                     +process.hltL1extraParticles
                     +process.L1MuonMCAnalysis
                     +process.L1EmMCAnalysis
                     +process.L1IsoEmMCAnalysis
                     +process.L1NonIsoEmMCAnalysis
                     +process.L1JetMCAnalysis
                     +process.L1CenJetMCAnalysis
                     +process.L1ForJetMCAnalysis
                     +process.L1TauJetMCAnalysis
                     +process.L1MetMCAnalysis)

process.e = cms.EndPath(process.l1GtTrigReport)
process.TFileService.fileName = 'l1RerunVal_STARTUP.root'
process.l1GtTrigReport.L1GtRecordInputTag = 'simGtDigis'

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:TTbar_cfi_GEN_SIM_DIGI_L1_DIGI2RAW_HLT.root')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)


