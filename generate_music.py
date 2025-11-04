#!/usr/bin/env python3
"""
Basit MusicVAE tabanlı müzik üretici.

Kullanım örneği:
python generate_music.py --config cat-mel_2bar_big --checkpoint ./checkpoints/cat-mel_2bar_big.ckpt --num_outputs 4 --length 32 --temperature 0.8 --out_dir outputs

README.md içinde ayrıntılı kurulum ve checkpoint indirme talimatları var.
"""
import os
import argparse
from datetime import datetime

try:
    import magenta.music as mm
    from magenta.models.music_vae import configs
    from magenta.models.music_vae.trained_model import TrainedModel
except Exception as e:
    raise ImportError("Magenta kütüphanesini yükleyin (pip install magenta). Hata: {}".format(e))

def generate(config_name, checkpoint_path, num_outputs, length, temperature, out_dir):
    config_map = configs.CONFIG_MAP
    if config_name not in config_map:
        raise ValueError("Bilinmeyen config adı: {}. Geçerli örnekler: {}".format(config_name, ", ".join(sorted(config_map.keys()))))

    config = config_map[config_name]
    os.makedirs(out_dir, exist_ok=True)

    print("Model konfigürasyonu:", config_name)
    print("Checkpoint:", checkpoint_path)
    print("Çıktı sayısı:", num_outputs, "Length (bar/steps):", length, "Temperature:", temperature)
    print("Çıktılar ->", out_dir)

    model = TrainedModel(config, batch_size=max(1, num_outputs), checkpoint_dir_or_path=checkpoint_path)

    # sample() API'si: birçok Magenta örneğinde sample ile NoteSequence üretilir.
    print("Örnekler üretiliyor...")
    sequences = model.sample(n=num_outputs, length=length, temperature=temperature)

    saved = []
    for i, seq in enumerate(sequences):
        timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        midi_filename = os.path.join(out_dir, f"sample_{i+1}_{timestamp}.mid")
        mm.sequence_proto_to_midi_file(seq, midi_filename)
        saved.append(midi_filename)
        print("Kaydedildi:", midi_filename)

    return saved

def main():
    parser = argparse.ArgumentParser(description="MusicVAE ile MIDI üretme")
    parser.add_argument("--config", type=str, default="cat-mel_2bar_big", help="MusicVAE config adı (örnek: cat-mel_2bar_big)")
    parser.add_argument("--checkpoint", type=str, required=True, help="Ön-eğitilmiş checkpoint .ckpt yolu")
    parser.add_argument("--num_outputs", type=int, default=4, help="Üretilecek MIDI sayısı")
    parser.add_argument("--length", type=int, default=32, help="Her örnek için uzunluk (steps/bar cinsinden modelin beklediği formatta)")
    parser.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature (0.1 - 2.0 arası deneyin)")
    parser.add_argument("--out_dir", type=str, default="outputs", help="Çıktı MIDI dosyalarının kaydedileceği klasör")
    args = parser.parse_args()

    midi_files = generate(args.config, args.checkpoint, args.num_outputs, args.length, args.temperature, args.out_dir)
    print("\nÜretim tamamlandı. MIDI dosyaları:")
    for m in midi_files:
        print(" -", m)

if __name__ == "__main__":
    main()