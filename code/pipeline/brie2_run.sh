
REF=genome/gencode.v31/AS_events/SE.lenient.gtf.gz
bam_info=result/brie2/dataset1/bam_cellID.tsv
out_dir=./result/brie2/dataset1/


brie-count  -a ${REF} -S ${bam_info} -o ${out_dir} -p 35
brie-quant -i ${out_dir}/brie_count.h5ad -o ${out_dir}/brie_quant_aggr.h5ad --interceptMode gene

