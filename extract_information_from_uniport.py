import requests
import json
import sys

# 从命令行获取 UniProt ID
if len(sys.argv) < 2:
    print("Usage: python script.py <UniProt_ID>")
    sys.exit(1)

uniprot_id = sys.argv[1]
#uniprot_id = "P68871"
url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"

response = requests.get(url)
data = response.json()

all_drugbank_values = []
all_go_values=[]
all_Reactome_values=[]
all_Orphanet_values=[]
all_KEGG_values=[]
all_GeneReviews_values=[]
all_HPA_values=[]

# 美化打印 JSON 输出
formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
#print(formatted_json)
#print(data.get("uniProtKBCrossReferences", {}).get("database", {}))
cross_refs = data.get("uniProtKBCrossReferences", [])
for ref in cross_refs:
    database = ref.get("database", "")
    entry_id = ref.get("id", "")
    properties = ref.get("properties","")

    if database == "HPA":
        values = [prop.get("value", "") for prop in properties]
        all_HPA_values.extend(values)

    if database == "GeneReviews":
        values = [prop.get("value", "") for prop in properties]
        all_GeneReviews_values.extend(values)

    if database == "KEGG":
        values = [prop.get("value", "") for prop in properties]
        all_KEGG_values.extend(values)

    if database == "Orphanet":
        values = [prop.get("value", "") for prop in properties]
        all_Orphanet_values.extend(values)

    if database == "Reactome":
        values = [prop.get("value", "") for prop in properties]
        all_Reactome_values.extend(values)

    if database == "GO":
        if properties:
            first_value = properties[0].get("value", "")
            all_go_values.append(first_value)
        #values = [prop.get("value", "") for prop in properties]
        #all_go_values.extend(entry_id)
        #all_go_values.extend(":")
        #all_go_values.extend(values)

    if database == "DrugBank":
        values = [prop.get("value", "") for prop in properties]
        all_drugbank_values.extend(values)

print(f"kegg: {all_KEGG_values}")
print(f"GO: {all_go_values}")
print(f"Reactome: {all_Reactome_values}")
print(f"Orphanet: {all_Orphanet_values}")
print(f"PaperReview: {all_GeneReviews_values}")
print(f"HPA: {all_HPA_values}")
print(f"DRUGBANK: {all_drugbank_values}")

#print("DRUGBANK:", all_drugbank_values)

    #if ((database != "PDB") and (database != "PDBsum") and (database != "EMBL") and (database != "EMDB") and (database != "CCDS") and (database != "PIR") and (database != "RefSeq") and (database != "AlphaFoldDB") and (database != "BMRB") and (database != "SASBDB") and (database != "SMR") and (database != "BioGRID") and (database != "ComplexPortal") and (database != "CORUM") and (database != "DIP") and (database != "FunCoup") and (database != "IntAct") and (database != "MINT") and (database != "STRING") and (database != "BindingDB") and (database != "ChEMBL") and (database != "PDBsum") and (database != "DrugCentral") and (database != "TCDB") and (database != "CarbonylDB") and (database != "GlyConnect") and (database != "GlyCosmos") and (database != "GlyGen") and (database != "iPTMnet") and (database != "MetOSite") and (database != "PhosphoSitePlus") and (database != "BioMuta") and (database != "DMDM") and (database != "REPRODUCTION-2DPAGE") and (database != "CPTAC") and (database != "jPOST") and (database != "MassIVE") and (database != "PaxDb") and (database != "PeptideAtlas") and (database != "ProteomicsDB") and (database != "TopDownProteomics") and (database != "ABCD") and (database != "Antibodypedia") and (database != "DNASU") and (database != "neXtProt") and (database != "neXtProt") and (database != "MIM") and (database != "MalaCards") and (database != "HGNC") and (database != "HGNC") and (database != "GeneCards") and (database != "DisGeNET") and (database != "CTD") and (database != "AGR") and (database != "UCSC") and (database != "MANE-Select") and (database != "GeneID") and (database != "PRIDE") and (database != "PathwayCommons") and (database != "TreeFam") and (database != "PhylomeDB") and (database != "PAN-GO") and (database != "OrthoDB") and (database != "OMA") and (database != "InParanoid") and (database != "HOGENOM") and (database != "GeneTree") and (database != "eggNOG") and (database != "VEuPathDB") and (database != "PharmGKB") and (database != "Proteomes") and (database != "PRO") and (database != "Pharos") and (database != "GenomeRNAi") and (database != "GeneWiki") and (database != "EvolutionaryTrace") and (database != "ChiTaRS") and (database != "BioGRID-ORCS") and (database != "SIGNOR") and (database != "SignaLink") and (database != "ExpressionAtlas") and (database != "Bgee") and (database != "RNAct") and (database != "Proteomes") and (database != "SUPFAM") and (database != "PRINTS") and (database != "Pfam") and (database != "PANTHER") and (database != "InterPro") and (database != "Gene3D") and (database != "FunFam") and (database != "CDD") and (database != "PROSITE")):
     #   print(f"{database}: {entry_id}: {properties}")
