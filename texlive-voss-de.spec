# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-voss-de
Version:	20111104
Release:	1
Summary:	TeXLive voss-de package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/voss-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/voss-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive voss-de package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/voss-de/InlineMath/Changes
%doc %{_texmfdistdir}/doc/generic/voss-de/InlineMath/InlineMath.bib
%doc %{_texmfdistdir}/doc/generic/voss-de/InlineMath/InlineMath.ltx
%doc %{_texmfdistdir}/doc/generic/voss-de/InlineMath/InlineMath.pdf
%doc %{_texmfdistdir}/doc/generic/voss-de/InlineMath/InlineMath.tex
%doc %{_texmfdistdir}/doc/generic/voss-de/InlineMath/README
%doc %{_texmfdistdir}/doc/generic/voss-de/README
%doc %{_texmfdistdir}/doc/generic/voss-de/gauss/Changes
%doc %{_texmfdistdir}/doc/generic/voss-de/gauss/README
%doc %{_texmfdistdir}/doc/generic/voss-de/gauss/gauss.ltx
%doc %{_texmfdistdir}/doc/generic/voss-de/gauss/gauss.pdf
%doc %{_texmfdistdir}/doc/generic/voss-de/gauss/gauss.tex
%doc %{_texmfdistdir}/doc/generic/voss-de/mathCol/Changes
%doc %{_texmfdistdir}/doc/generic/voss-de/mathCol/README
%doc %{_texmfdistdir}/doc/generic/voss-de/mathCol/mathCol.bib
%doc %{_texmfdistdir}/doc/generic/voss-de/mathCol/mathCol.ltx
%doc %{_texmfdistdir}/doc/generic/voss-de/mathCol/mathCol.pdf
%doc %{_texmfdistdir}/doc/generic/voss-de/mathCol/mathCol.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
