#!/usr/bin/env bash
# Örnek: cat-mel_2bar_big için checkpoint indirici (gsutil gerektirir) veya tar.gz linki ile curl/wget kullan.
# NOT: Aşağıdaki örnekler genel yol gösterir. Magenta model checkpoint URL'leri zamanla değişebilir.
set -e

mkdir -p checkpoints
cd checkpoints

echo "cat-mel_2bar_big için örnek indirme (eğer gsutil yoksa alternatif .tar.gz URL'si bulun)"
# Google Cloud Storage üzerinden indirilebiliyorsa:
# gsutil cp gs://magentadata/models/music_vae/checkpoints/cat-mel_2bar_big.tar .
# Eğer gsutil yoksa, tar dosyasının public HTTP URL'si varsa curl/wget ile çek.
# Aşağıdaki yorum satırı örnek amaçlıdır (gerçek URL'yi magenta docs'dan kontrol et):
# curl -O https://storage.googleapis.com/magentadata/models/music_vae/checkpoints/cat-mel_2bar_big.tar

echo "İndirmeyi yaptıktan sonra .tar içeriğini çıkarın ve generate_music.py --checkpoint parametresine uygun dosya yolunu verin."
echo "Örnek kullanım: python ../generate_music.py --checkpoint ./cat-mel_2bar_big.ckpt --num_outputs 4"
