%global tl_name media9
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.30
Release:	%{tl_revision}.1
Summary:	Multimedia inclusion package with Adobe Reader-9/X compatibility
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/media9
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/media9.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/media9.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/media9.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an interface to embed interactive Flash (SWF) and
3D objects (Adobe U3D & PRC), as well as video and sound files or
streams in the popular MP4, FLV and MP3 formats into PDF documents with
Acrobat-9/X compatibility. Playback of multimedia files uses the built-
in Flash Player of Adobe Reader and does, therefore, not depend on
external plug-ins. Flash Player supports the efficient H.264 codec for
video compression. The package is based on the RichMedia Annotation, an
Adobe addition to the PDF specification. It replaces the now obsolete
movie15 package.

