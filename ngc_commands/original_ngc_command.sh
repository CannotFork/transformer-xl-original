cd transformer-xl-original \
  && export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \
  && mkdir -p data \
  && cd data \
  && wget --continue https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-v1.zip \
  && unzip -q wikitext-103-v1.zip \
  && cd wikitext-103 \
  && mv wiki.train.tokens train.txt \
  && mv wiki.valid.tokens valid.txt \
  && mv wiki.test.tokens test.txt \
  && cd ../.. \
  && cd pytorch \
  && bash run_wt103_base_ngc.sh train  

