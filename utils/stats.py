import sys
import os


class FileStats:

    file = None
    lines = 0
    characters = 0
    
    def __init__( self, file ): 
        self.file = file
    
    
class FileTypeStats:

    extension = None
    files = 0
    lines = 0
    characters = 0

    def __init__( self, extension ): 
        self.extension = extension


class FileScanner:


    def scan( self, file_name ):
    
        stats = FileStats( file_name )
    
        with open( file_name ) as file:
            for line in file:
                self.scan_line( line, stats )
                
        return stats
    
    
    def scan_line( self, line, stats ):
    
        cleaned = self.clean_line( line )
        
        if len( cleaned ) > 0:

            stats.lines += 1
            
            for c in cleaned:
                if not c.isspace():
                    stats.characters += 1
                
            
    def clean_line( self, line ):
    
        return line.strip()


class PythonScanner( FileScanner ):


    def clean_line( self, line ):
    
        result = line.strip()
        
        if result.startswith( "#" ):
            result = ""

        return result


SCANNERS = {}
GENERIC_FILE_SCANNER = FileScanner()

SCANNERS[ "py" ] = PythonScanner()
SCANNERS[ "js" ] = GENERIC_FILE_SCANNER
SCANNERS[ "json" ] = GENERIC_FILE_SCANNER
SCANNERS[ "css" ] = GENERIC_FILE_SCANNER
SCANNERS[ "svg" ] = GENERIC_FILE_SCANNER
SCANNERS[ "html" ] = GENERIC_FILE_SCANNER
SCANNERS[ "sh" ] = GENERIC_FILE_SCANNER


def scan( folder ):

    stats_by_file = {}
    stats_by_type = {}
    excluded_types = set()

    for root, dirs, files in os.walk( folder ):
    
        for file in files:
        
            path = os.path.join( root, file )
            file_name, file_extension = os.path.splitext( file )
            
            if file_extension:
                
                extension = file_extension[ 1: ]
                scanner = SCANNERS.get( extension )
                
                if scanner:
                    
                    path = os.path.join( root, file )
                    file_stats = scanner.scan( path )
                    
                    stats_by_file[ path ] = file_stats
                    
                    file_type_stats = stats_by_type.get( extension )
                    
                    if not file_type_stats: 
                        file_type_stats = FileTypeStats( extension )
                        stats_by_type[ extension ] = file_type_stats
                    
                    file_type_stats.files += 1
                    file_type_stats.lines += file_stats.lines
                    file_type_stats.characters += file_stats.characters
                    
                else:
                
                    excluded_types.add( extension )
                    
            else:
            
                excluded_types.add( file_name )
            
    total_files = 0
    total_lines = 0
    total_characters = 0
    
    for stats in stats_by_type.values():
    
        total_files += stats.files
        total_lines += stats.lines
        total_characters += stats.characters
    
    print( "" )
    print( "Comments and whitespace are excluded from line and character counts" )
    
    print( "" )
    print( "Files: {0:,}".format( total_files ) )
    print( "" )
    
    for extension, stats in sorted( stats_by_type.items(), key = lambda ( k, v ): ( v.files * -1, v.extension ) ):
        print( "  {0}: {1:,}".format( extension, stats.files ) )
        
    print( "" )
    print( "Lines: {0:,}".format( total_lines ) )
    print( "" )
    
    for extension, stats in sorted( stats_by_type.items(), key = lambda ( k, v ): ( v.lines * -1, v.extension ) ):
        print( "  {0}: {1:,}".format( extension, stats.lines ) )
        
    print( "" )
    print( "Characters: {0:,}".format( total_characters ) )
    print( "" )
    
    for extension, stats in sorted( stats_by_type.items(), key = lambda ( k, v ): ( v.characters * -1, v.extension ) ):
        print( "  {0}: {1:,}".format( extension, stats.characters ) )

    print( "" )
    print( "Excluded File Types: {0:,}".format( len( excluded_types ) ) )
    print( "" )
    
    for extension in sorted( excluded_types ):
        print( "  {0}".format( extension ) )

    print( "" )


if __name__ == "__main__": scan( sys.argv[ 1 ] )
