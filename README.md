# AI ile Açık Kaynak Müzik Üretimi (MusicVAE örneği)

Bu küçük proje, Magenta'nın MusicVAE ön-eğitilmiş modellerini kullanarak MIDI müzikleri üretir. Üretilen MIDI dosyalarını FluidSynth veya Timidity gibi araçlarla WAV'e çevirip dinleyebilirsin.

Özet:
- Python betiği: generate_music.py
- Bağımlılıklar: magenta, tensorflow, note-seq, pretty_midi, vb.
- Model: MusicVAE ön-eğitilmiş checkpoint (ayrı indirilir)

Kurulum (Linux/macOS):
1. Sanal ortam oluştur (tercih edilir)
   python -m venv venv
   source venv/bin/activate

2. Bağımlılıkları yükle
   pip install -r requirements.txt

3. Checkpoint indir
   - Magenta model checkpoint'leri genellikle Google Cloud Storage üzerinde bulunur. En güncel linkleri Magenta'nın resmi dökümantasyonundan kontrol et.
   - Örnek: `download_checkpoints.sh` dosyasındaki yönergeleri takip et veya Magenta web sayfasından `cat-mel_2bar_big` gibi ön-eğitilmiş bir checkpoint indirip çıkar.

4. Modeli kullanarak MIDI üret
   python generate_music.py --checkpoint /path/to/cat-mel_2bar_big.ckpt --config cat-mel_2bar_big --num_outputs 4 --length 32 --temperature 0.8 --out_dir outputs

5. (Opsiyonel) MIDI -> WAV dönüştürme
   - FluidSynth örneği:
     sudo apt install fluidsynth
     fluidsynth -ni /path/to/soundfont.sf2 outputs/sample_1_....mid -F outputs/sample_1.wav -r 44100

   - Timidity örneği:
     sudo apt install timidity
     timidity outputs/sample_1_....mid -Ow -o outputs/sample_1.wav

Notlar:
- `--temperature` değeri: 0.5–1.5 arası deneyerek daha deterministik veya daha rastgele sonuçlar alabilirsin.
- `--length` parametresi model ve config'e göre değişiklik gösterir; config dokümantasyonunu kontrol et.
- Magenta ve TF sürümleri uyumluluğu önemlidir; gereksinimler `requirements.txt` içinde var ancak sistemine göre TF sürümünü ayarlaman gerekebilir.

Kaynaklar:
- Magenta: https://github.com/magenta/magenta
- MusicVAE modelleri ve checkpoint'ler: Magenta dökümantasyonu / model indirme sayfaları

Lisans: Bu örnek açık kaynaklıdır, istediğin gibi uyarlayabilir ve dağıtabilirsin. Kullanılan modellerin lisanslarını da kontrol et.
