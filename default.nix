{ pkgs ? import <nixpkgs> {} }:

let
  python-with-deps = pkgs.python3.withPackages (ps: [ ps.python-rtmidi ]);
in
pkgs.stdenv.mkDerivation {
  pname = "midi-udp-streamer";
  version = "1.0.0";
  src = ./.;
  buildInputs = [ python-with-deps ];
  installPhase = ''
    mkdir -p $out/bin
    cp stream_midi_udp.py $out/bin/
    chmod +x $out/bin/stream_midi_udp.py
  '';
}
