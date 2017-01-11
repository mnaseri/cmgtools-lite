from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 

topCore_globalVariables = [
            NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
            NTupleVariable("rhoCN",  lambda ev: ev.rhoCN, float, help="fixed grid rho central neutral"),
            NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"), 

#            NTupleVariable("nJet25", lambda ev: len(ev.cleanJets), int, help="Number of jets with pt > 25"),
#            NTupleVariable("nBJetLoose25", lambda ev: len(ev.bjetsLoose), int, help="Number of jets with pt > 25 passing CSV loose"),
#            NTupleVariable("nBJetMedium25", lambda ev: len(ev.bjetsMedium), int, help="Number of jets with pt > 25 passing CSV medium"),
#            NTupleVariable("nBJetTight25", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium]), int, help="Number of jets with pt > 25 passing CSV tight"),

            NTupleVariable("nJet25", lambda ev: sum([j.pt() > 25 for j in ev.cleanJets]), int, help="Number of jets with pt > 25, |eta|<2.4"),
            NTupleVariable("nJet25a", lambda ev: sum([j.pt() > 25 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 25, |eta|<4.7"),
            NTupleVariable("nBJetLoose25", lambda ev: sum([j.btagWP("CSVv2IVFL") for j in ev.cleanJets if j.pt() > 25]), int, help="Number of jets with pt > 25 passing CSV loose"),
            NTupleVariable("nBJetMedium25", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.bjetsMedium if j.pt() > 25]), int, help="Number of jets with pt > 25 passing CSV medium"),
            NTupleVariable("nBJetTight25", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium if j.pt() > 25]), int, help="Number of jets with pt > 25 passing CSV tight"),

            NTupleVariable("nJet30", lambda ev: sum([j.pt() > 30 for j in ev.cleanJets]), int, help="Number of jets with pt > 30, |eta|<2.4"),
            NTupleVariable("nJet30a", lambda ev: sum([j.pt() > 30 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 30, |eta|<4.7"),
            NTupleVariable("nBJetLoose30", lambda ev: sum([j.btagWP("CSVv2IVFL") for j in ev.cleanJets if j.pt() > 30]), int, help="Number of jets with pt > 30 passing CSV loose"),
            NTupleVariable("nBJetMedium30", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.bjetsMedium if j.pt() > 30]), int, help="Number of jets with pt > 30 passing CSV medium"),
            NTupleVariable("nBJetTight30", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium if j.pt() > 30]), int, help="Number of jets with pt > 30 passing CSV tight"),

#            NTupleVariable("nJet40", lambda ev: sum([j.pt() > 40 for j in ev.cleanJets]), int, help="Number of jets with pt > 40, |eta|<2.4"),
#            NTupleVariable("nJet40a", lambda ev: sum([j.pt() > 40 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 40, |eta|<4.7"),
#            NTupleVariable("nBJetLoose40", lambda ev: sum([j.btagWP("CSVv2IVFL") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV loose"),
#            NTupleVariable("nBJetMedium40", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.bjetsMedium if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium"),
#            NTupleVariable("nBJetTight40", lambda ev: sum([j.btagWP("CSVv2IVFT") for j in ev.bjetsMedium if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV tight"),

            ##--------------------------------------------------
            NTupleVariable("nLepGood20", lambda ev: sum([l.pt() > 20 for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 20"),
            NTupleVariable("nLepGood15", lambda ev: sum([l.pt() > 15 for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 15"),
            NTupleVariable("nLepGood10", lambda ev: sum([l.pt() > 10 for l in ev.selectedLeptons]), int, help="Number of leptons with pt > 10"),
            
#           NTupleVariable("eleCutIdSpring16_25ns_v1_ConvVeto",     lambda x : (1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Veto") + 1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Loose") + 1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Medium") + 1*x.electronID("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Tight")) if abs(x.pdgId()) == 11 and x.isElectronIDAvailable("POG_Cuts_ID_SPRING16_25ns_v1_ConvVeto_Veto") else -1, int, help="Electron cut-based id (POG Spring16_25ns_v1): 0=none, 1=veto, 2=loose, 3=medium, 4=tight") 
##--------------------------------------------------
            #NTupleVariable("GenHeaviestQCDFlavour", lambda ev : ev.heaviestQCDFlavour, int, mcOnly=True, help="pdgId of heaviest parton in the event (after shower)"),
            #NTupleVariable("LepEff_1lep", lambda ev : ev.LepEff_1lep, mcOnly=True, help="Lepton preselection SF (1 lep)"),
            #NTupleVariable("LepEff_2lep", lambda ev : ev.LepEff_2lep, mcOnly=True, help="Lepton preselection SF (2 lep)"),
            ##------------------------------------------------
]

topCore_globalObjects = {
            "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
            "metNoPU" : NTupleObject("metNoPU", fourVectorType, help="PF noPU E_{T}^{miss}"),
}

topCore_collections = {
            "genleps"         : NTupleCollection("genLep",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays"),                                                                                                
            "genJets" : NTupleCollection("genJet", genParticleType, 10, help="Generated jets (not cleaned)"),

            "cleanGenJets" : NTupleCollection("cleangenJet", genParticleType, 10, help="Cleaned Generated jets"),

            "gentauleps"      : NTupleCollection("genLepFromTau", genParticleWithLinksType, 10, help="Generated leptons (e/mu) from decays of taus from W/Z/h decays"),                                                                       
            "gentaus"         : NTupleCollection("genTau",     genParticleWithLinksType, 10, help="Generated leptons (tau) from W/Z decays"),                            
            "gennus"          : NTupleCollection("genNeu",     genParticleWithLinksType, 10, help="Generated prompt neutrinos"),

            "genbquarks"      : NTupleCollection("genbquark",     genParticleWithLinksType, 10, help="b quarks from hard event (e.g. from top decays)"),

            "gentopquarks"    : NTupleCollection("GenTop",     genParticleType, 2, help="Generated top quarks from hard scattering (needed separately for top pt reweighting)"),

            "genbquarksFromTop"  : NTupleCollection("GenbquarkFromTop",     genParticleType, 2, help="generated b-quarks from t->bW decay"),

            "gennusFromTop"  : NTupleCollection("GennusFromTop",     genParticleType, 2, help="generated Neutrinos from t->W decay"),

            "genlepsFromTop" : NTupleCollection("GenLepFromTop",     genParticleType, 2, help="#mu/ele that have a t->W chain as ancestor, also contained in event.genleps"),

           "generatorSummary" : NTupleCollection("GenPart", genParticleWithLinksType, 100 , help="Hard scattering particles, with ancestry and links"),

           "genParticles" : NTupleCollection("genPart", genParticleWithMotherId, 300, help="all pruned genparticles"),
}
