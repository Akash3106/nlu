"""
Resolve Annotator Classes in the Pipeline to Extractor Configs and Methods

Every Annotator should have 2 configs. Some might offor multuple configs/method pairs, based on model/NLP reference.
- default/minimalistic -> Just the results of the annotations, no confidences or extra metadata
- with meta            -> A config that leverages white/black list and gets the most relevant metadata
- with positions       -> With Begins/Ends
- with sentence references -> Reeturn the sentence/chunk no. reference from the metadata.
                                If a document has multi-sentences, this will map a label back to a corrosponding sentence

"""
from nlu.pipe.extractors.extractor_configs_open_source import *
from nlu.pipe.extractors.extractor_configs_healthcare import *
from nlu.pipe.col_substitution.col_substitution_HC import *
from nlu.pipe.col_substitution.col_substitution_OS import *

from sparknlp_jsl.annotator  import *

HC_anno2substitution_fn = {
    MedicalNerModel : {
        'default': substitute_ner_dl_cols ,
    },
    NerConverterInternal : {
        'default': substitute_ner_internal_converter_cols,
    },
    AssertionDLModel : {
        'default': substitute_assertion_cols,
    },
    AssertionLogRegModel : {
        'default': substitute_assertion_cols,
    },
    SentenceEntityResolverModel : {
        'default': substitute_sentence_resolution_cols,
    },
    ChunkEntityResolverModel : {
        'default': substitute_chunk_resolution_cols,
    },

    DeIdentificationModel : {
        'default': substitute_de_identification_cols,
    },
    RelationExtractionModel : {
        'default': 'TODO',
    },

    RelationExtractionDLModel : {
        'default': 'TODO',
    },
    Chunk2Token : {
        'default': '',# TODO
    },

    ContextualParserModel : {
        'default': '',# TODO

    },

    DrugNormalizer : {
        'default': '',# TODO
    },

    GenericClassifierModel : {
        'default': '',# TODO
    },


    ChunkMergeModel : {
        'default': '',# TODO
    },

    NerDisambiguatorModel : {
        'default': '',# TODO
    },

    RENerChunksFilter : {
        'default': '',# TODO
    },

    NerOverwriter : {
        'default': '',# TODO
    },
    PosologyREModel : {
        'default': 'TODO',
    }

}







