// ocr <img...> : imprime uma linha JSON por imagem com o texto reconhecido (Vision, pt-BR + en-US), de cima para baixo
import Foundation
import Vision
import AppKit
for path in CommandLine.arguments.dropFirst() {
    guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { continue }
    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.recognitionLanguages = ["pt-BR", "en-US"]
    req.usesLanguageCorrection = true
    try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
    let obs = (req.results ?? []).sorted { abs($0.boundingBox.maxY - $1.boundingBox.maxY) > 0.015 ? $0.boundingBox.maxY > $1.boundingBox.maxY : $0.boundingBox.minX < $1.boundingBox.minX }
    let lines = obs.compactMap { $0.topCandidates(1).first?.string }
    let data = try! JSONSerialization.data(withJSONObject: ["f": path, "lines": lines])
    print(String(data: data, encoding: .utf8)!)
}
