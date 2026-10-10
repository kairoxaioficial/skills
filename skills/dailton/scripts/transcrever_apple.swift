// Transcreve um arquivo de áudio em pt-BR com o SpeechAnalyzer do macOS 26 (on-device, Neural Engine).
// uso: transcrever_apple <audio.wav> <saida-sem-extensao>   -> grava <saida>.txt ([h:mm:ss] texto) e <saida>.json
import AVFoundation
import Foundation
import Speech

struct Seg: Codable { let ini: Double; let fim: Double; let texto: String }

@main
struct TranscreverApple {
    static func main() async {
        let args = CommandLine.arguments
        guard args.count >= 3 else { print("uso: transcrever_apple <audio> <saida>"); exit(2) }
        do {
            guard let locale = await SpeechTranscriber.supportedLocale(equivalentTo: Locale(identifier: "pt-BR")) else {
                print("pt-BR não suportado"); exit(1)
            }
            let transcriber = SpeechTranscriber(locale: locale, preset: .transcription)
            if let pedido = try await AssetInventory.assetInstallationRequest(supporting: [transcriber]) {
                print("baixando o modelo de fala pt-BR", terminator: "\n"); fflush(stdout)
                try await pedido.downloadAndInstall()
            }
            let analyzer = SpeechAnalyzer(modules: [transcriber])
            let arquivo = try AVAudioFile(forReading: URL(fileURLWithPath: args[1]))
            let t0 = Date()
            let coletor = Task { () -> [Seg] in
                var out: [Seg] = []
                for try await r in transcriber.results {
                    let texto = String(r.text.characters).trimmingCharacters(in: .whitespacesAndNewlines)
                    if texto.isEmpty { continue }
                    out.append(Seg(ini: r.range.start.seconds, fim: CMTimeRangeGetEnd(r.range).seconds, texto: texto))
                    if out.count % 40 == 0 {
                        print("progresso \(Int(r.range.start.seconds / 60)) min de áudio em \(Int(Date().timeIntervalSince(t0)))s")
                        fflush(stdout)
                    }
                }
                return out
            }
            if let fim = try await analyzer.analyzeSequence(from: arquivo) {
                try await analyzer.finalizeAndFinish(through: fim)
            } else {
                await analyzer.cancelAndFinishNow()
            }
            let segs = try await coletor.value
            let saida = args[2]
            var txt = ""
            for s in segs {
                let t = Int(s.ini)
                txt += String(format: "[%d:%02d:%02d] ", t / 3600, (t % 3600) / 60, t % 60) + s.texto + "\n"
            }
            try txt.write(toFile: saida + ".txt", atomically: true, encoding: .utf8)
            let enc = JSONEncoder(); enc.outputFormatting = [.prettyPrinted]
            try enc.encode(["segmentos": segs]).write(to: URL(fileURLWithPath: saida + ".json"))
            print("ok \(segs.count) segmentos, \(Int(segs.last?.fim ?? 0))s de áudio em \(Int(Date().timeIntervalSince(t0)))s")
        } catch {
            print("erro: \(error)"); exit(1)
        }
    }
}
